import pprint

def isValidChessBoard(board):
  piecesCount = {'b': 0, 'w': 0}
  pawnCount = {'b': 0, 'w': 0}
  hasKing = {'b': False, 'w': False}
  letterAxis = ('a','b','c','d','e','f','g','h')
  pieceColor = ('b', 'w')
  pieceType = ('pawn', 'knight', 'bishop', 'rook', 'queen', 'king')

  # each player has <== 16 pieces
  for pos, i in board.items():
    # check position value
    # all pieces must be on valid space from '1a' to '8h'
    if int(pos[0]) >= 9:
      print('SpacesError')
      return False
    
    if pos[1] not in letterAxis:
      print('yAxisError')
      return False
    
    # check piece data
    if i != '':
      # piece names begin with 'w' or 'b'
      if i[0] not in pieceColor:
        print('WhiteOrBlackError')
        return False
      
      thisPieceColor = i[0]
      piecesCount[thisPieceColor] += 1

      if piecesCount[thisPieceColor] >= 17:
        print('TotalPieceError')
        return False
      
      # piece names must follow with 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'
      thisPieceType = i[1:]

      if thisPieceType not in pieceType:
        print('PieceTypeError')
        print(thisPieceType)
        return False
      elif thisPieceType == 'pawn':
        pawnCount[thisPieceColor] += 1

        # each players has <= 8 pawns
        if pawnCount[thisPieceColor] >= 9:
          print('PawnError')
          return False 
      elif thisPieceType == 'king':
        # one black king and one white king
        if hasKing[thisPieceColor] == True:
          print('AlreadyHasKingError')

        hasKing[thisPieceColor] = True
  if list(hasKing.values()) != [True, True]:
    print('MissingKingError')
    return False
  return 'This board checks out'



chessBoard = {'1a': 'bking','2a': 'bqueen','3a': 'brook','4a': 'brook',
'5a': 'bknight','6a': 'bknight','7a':'bbishop','8a': 'bbishop',
'1b': 'bpawn','2b': 'bpawn','3b': 'bpawn','4b':'bpawn',
'5b': 'bpawn','6b': 'bpawn','7b': 'bpawn','8b': 'bpawn',
'1c': 'wking','2c': 'wqueen','3c': 'wrook','4c': 'wrook',
'5c': 'wbishop','6c': 'wbishop','7c': 'wknight','8c':'wknight',
'1e': 'wpawn','2e': 'wpawn','3e': 'wpawn','4e': 'wpawn',
'5e': 'wpawn','6e': 'wpawn','7e': 'wpawn','8e': 'wpawn',
'1f': '','2f': '','3f': '','4f': '','5f': '','6f': '','7f': '','8f': '',
'1g': '','2g': '','3g': '','4g': '','5g': '','6g': '','7g': '','8g': '',
'1h': '','2h': '','3h': '','4h': '','5h': '','6h': '','7h': '','8h': '',}

# print(chessBoard)

def countChessPieces(board):
  count = {}
  for k, v in board.items():
    count.setdefault(v, 0)
    count[v] += 1
  return count
  

pprint.pprint(countChessPieces(chessBoard))

print(isValidChessBoard(chessBoard))