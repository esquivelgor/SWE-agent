<program> -> <segment>
           | <segment> <program>
<segment> -> <misc>* <class_def> <misc>*
<class_def> -> <class> <identifier> <colon> <suite>
            |  <class> <identifier> <lparen> <identifier> <rparen> <colon> <suite>
<misc> -> <import_stmt>
        | <function_def>
        | <statement> 
<suite> -> <statement>+
<import_stmt> -> <import> <identifier> (<period> <identifier>)*
               | <from> <identifier> (<period> <identifier>)* <import> <identifier> (<comma> <identifier>)*
<function_def> -> <def> <identifer> <lparen> <rparen> <colon> <suite>
                | <def> <identifer> <lparen> <parameters> <rparen> <colon> <suite>
<statement> -> <attribute_as>
             | <simple_stmt>
             | <funciton_def>
             | <class_def> 
<attribute_as> -> <identifier> <as> <expression>
<simple_stmt> -> <return> <expression>
               | <expression>
               | <pass>
<parameters> -> <identifier> (<comma> <identifier>)*
<expression> -> <identifier>
              | <literal>
<identifier> -> [a-zA-Z_][a-zA-Z0-9]*
<literal> -> <number>
           | <string>
<number> -> [0-9]+
<string> -> "\"" .* "\""
         -> "\'" .* "\'"
<class> -> "class"
<comma> -> ","
<import> -> "import"
<from> -> "from"
<colon> -> ":"
<lparen> -> "("
<rparen> -> ")"
<as> -> "="
<return> -> "return"
<pass> -> "pass"
