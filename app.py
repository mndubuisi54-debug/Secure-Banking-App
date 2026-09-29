from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import random

app = Flask(__name__)
app.secret_key = 'secure-banking-secret-key'

DATABASE = "database/Securebank.db"

def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection
@app.route('/')

@app.route('/dashboard')

def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    connection = get_db_connection()

    user = connection.execute(
        'SELECT * FROM users WHERE id = ?',
        (session['user_id'],)
    ).fetchone()

    account = connection.execute(
        'SELECT * FROM accounts WHERE user_id = ?',
        (session['user_id'],)
    ).fetchone()

    transactions = connection.execute(
            'SELECT * FROM transactions WHERE sender_account = ? OR receiver_account = ? ORDER BY created_at DESC',
            (account['account_number'], account['account_number'])
    ).fetchall()
    
    connection.close()
    
    return render_template (
        'index.html',
        user=user,
        account=account,
        transactions=transactions
    )

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        password_hash = generate_password_hash(password)

        account_number = str(random.randint(1000000000, 9999999999))

        connection = get_db_connection()

        # Create the user
        cursor = connection.execute(
            'INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)',
                           (name, email, password_hash)
        )

        # Get the user ID of the newly created user
        user_id = cursor.lastrowid

        # Create a bank account for the user
        connection.execute(
            'INSERT INTO accounts (user_id, account_number, balance) VALUES (?, ?, ?)',
            (user_id, account_number, 0.00)
        )  
        
        connection.commit()
        connection.close()

        return redirect(url_for('dashboard'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        connection = get_db_connection()
        user = connection.execute(
            'SELECT * FROM users WHERE email = ?', (email,)
        ).fetchone()
        connection.close()

        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            flash('Login successful! Welcome back.', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password. Please try again.', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'danger')
    return redirect(url_for('login'))

@app.route('/verify-account', methods=['GET', 'POST'])
def verify_account():
    account_number = request.args.get('account_number')

    connection = get_db_connection()
    account = connection.execute(
        'SELECT * FROM accounts WHERE account_number = ?',
        (account_number,)
    ).fetchone()

    if not account:
        connection.close()
        return{"found": False}

    user = connection.execute(
        'SELECT * FROM accounts WHERE user_id = ?',
        (account['user_id'],)
    ).fetchone()

    connection.close()

    return{
        'found: True,'
        'name': user['name']
    }
@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    connection = get_db_connection()

    sender_account = connection.execute(
        'SELECT * FROM accounts WHERE user_id = ?',
        (session['user_id'],)
    ).fetchone()

    if request.method == 'POST':
        receiver_account_number = request.form['account_number']
        amount = float(request.form['amount'])
        description = request.form.get('description', '')
        receiver_account = connection.execute(
            'SELECT * FROM accounts WHERE account_number = ?',
            (receiver_account_number,)
        ).fetchone()
        receiver_user = connection.execute(
            'SELECT name FROM users WHERE id = ?',
            (receiver_account['user_id'],)
        ).fetchone()

        if not receiver_account:

            flash(
                'Recipent account not found.',
                'danger'
            )
            connection.close()
            return redirect(url_for('transfer'))
        receiver_user = connection.execute(
                    'SELECT name FROM users WHERE id = ?',
                    (receiver_account['user_id'],)
        ).fetchone
        if receiver_account['account_number'] == sender_account['account_number']:
            flash(
                'You cannot transfer to self!!.',
                'danger'
            )
            connection.close()
            return redirect(url_for('transfer'))
        if amount > sender_account['balance']:
            flash(
                'Insufficient funds for this transfer.',
                'danger'
            )
            connection.close()
            return redirect(url_for('transfer'))
        if amount <= 0:
            flash(
                'Transfer amount must be greater than 0',
                'danger'
            )
            connection.close()
            return redirect(url_for('transfer'))
        connection.execute(
            'UPDATE accounts SET balance = balance - ? WHERE id = ?',
            (amount, sender_account['id'])
        )
        connection.execute(
            'UPDATE accounts SET balance = balance + ? WHERE id = ?',
            (amount, receiver_account['id'])
        )
        connection.execute(
            '''
            INSERT INTO transactions
            (sender_account, receiver_account, amount, transaction_type, status, description)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''',
            (
                sender_account['account_number'],
                receiver_account['account_number'],
                amount,
                'transfer',
                'completed',
                description
            )
        )
        connection.commit()
        connection.close()
        flash(
            'Transfer completed successfully.',
            'success'
        )
        return redirect(url_for('transfer'))
    connection.close()
    return render_template(
        'transfer.html',
        receiver_user=receiver_user if request.method == 'POST' and 'receiver_user' in locals() else None
        )

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    connection = get_db_connection()

    account = connection.execute(
        'SELECT * FROM accounts WHERE user_id = ?',
        (session['user_id'],)
    ).fetchone()
    if request.method == 'POST':
        amount = float(request.form['amount'])
        if amount <= 0:
            flash(
                'Amount must be greater than 0.',
                'danger'
            )
            connection.close()
            return redirect(url_for('deposit'))

        connection.execute(
            'UPDATE accounts SET balance = balance + ? WHERE id = ?',
            (amount, account['id'])
        )
        connection.commit()
        connection.close()
        flash('Deposit completed successfully.', 'success')
        return redirect(url_for('dashboard'))

    connection.close()
    return render_template('deposit.html', account=account)
if __name__ == '__main__':
    app.run(debug=True)