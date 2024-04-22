### Library Management System

#### Requirements

1. Search book by title, author, subject category, ISBN
2. unique identification number and other details including a rack number which will help to physically locate the book.
3. There could be more than one copy of a book, and library members should be able to check-out and reserve any copy.
4. The system should be able to retrieve information like who took a particular book 
5. what are the books checked-out by a specific library member.
6. Limit on at a time how many books a person can checkout
7. Limit on for how many days a person can keep a book.
8. Collect fines on book returned after due date
9. Notification on when a reserved book becomes available, and on book not returned on due date
10. Book and member card has bar code, system should be able to read the barcode from both.


#### Users 
1. Librarian: to add and modify book and items also member details, book issue details, reserve book,
2. Member: search, reserve, and issue, renew and return a book
3. System: to send notification for reservation, cancellation and renew



```mermaid

classDiagram
    class Library{
        +name: String
        +address: String
        get_address(): Address
    }
    BookItem *-- Library : composition
    class Librarian{
        addBookItem(): bool
        blockmember(): bool
        unblockmember(): bool
    }
    Librarian --|> Account : implements
    class Book{
        ISBN: string
        title: string
        subject: string
        publisher: string
        language: string
        number_of_pages: int
        get_title(): string
        
    }
    Book "*" <|--|> "*" Author
    class BookItem{
        +barcode: String
        isReferenceOnly: bool
        borrowed: DateTime
        due_date: DateTime
        price: Double
        format: enum ['Harcover', 'Paperback',
                        'Audiobook', 'Ebook', 'Journal']
        status: enum ['Available', 'Reserved',
                        'Loaned', 'Lost']
        date_of_purchase: DateTime
        publication_date: DateTime
    }
    BookItem --|> Rack
    class Account{
        id: int
        password: string
        status: AccountStatus ['Active', 'Closed', 'Cancelled', 'Blacklisted', 'None']
        user: User
        
        reset_password(): bool
    }
    
    Account --|> BookItem : borrows
    Account --|> BookItem : reserves
    Account "*" --|> "*" BookLending
    
    class Member{
        date_of_membership: DateTime
        total_book_checkout: int
        get_total_checkedout_books(): int
    }
    
    Member --|> Account : composition
    
    class LibraryCard{
        card_number: string
        barcode: string
        issued_at: Date
        active: Bool
        is_active(): bool
    }
    
    LibraryCard "1" --|> "1" Account : composition
    
    class BookReservation{
        creattion_date: Date
        status: ReservationStatus ['Waiting', 'Pending', 'Complete', 'Cancelled', 'None']
        get_status(): ReservationStatus
        fetch_reservation_details: BookReservation
    }
    
    Account --|> BookReservation : makes
    
    class BookLending{
        creation_date: Date
        due_date: Date
        return_date: date
        get_return_Date(): date
    }
    
    BookLending --|> BookItem : against
    BookLending "1" --|> "0..1" Fine 
    
    class Search{
        search_by_title(string)
        search_by_author(string)
        search_by_subject(string)
        search_by_pub_date(string)
    }
    class Fine{
        amount: double
        get_amount(): double
    }
    class FineTransaction{
        creation_date: date
        amount: double
        
        initiate_transaction(): bool
    }
    class CreditCardTransaction{
        name_on_card: string
    }
    
    CreditCardTransaction --|> FineTransaction : extends
    
    class UPITransaction{
        upi: string
    }
    
    UPITransaction --|> FineTransaction : extends
    
    class Author{
        +name: String
        +description: String
        +get_name(): String
    }
    class Rack{
        number: int
        location_identifier: string
    }
    class Notification{
        notification_id: int
        created_on: date
        content: string
        
        send_notification(): bool
    }
    class EmailNotification{
        email: string
    }
        
    class BarcodeReader{
        id: string
        registered_at: Date
        active: bool
        is_Active: bool
    }
    
    BarcodeReader --|> LibraryCard : scans
        
        



```