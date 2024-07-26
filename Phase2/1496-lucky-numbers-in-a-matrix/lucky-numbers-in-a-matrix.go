func luckyNumbers (matrix [][]int) []int {

    

    var row [ ] int

    for i:= 0 ; i< len(matrix);i ++ {
        var row_min int = 2147483647
        // var col_min int = 2147483647
        for j:= 0; j< len(matrix[0]);j++{
            if row_min > matrix[i][j]{
                row_min = matrix[i][j]
            }
        
        }
        row = append(row,row_min)
    }

    var col [ ] int

    for i:= 0 ; i< len(matrix[0]);i ++ {
        var row_min int = -2147483647
        // var col_min int = 2147483647
        for j:= 0; j< len(matrix);j++{
            if row_min < matrix[j][i]{
                row_min = matrix[j][i]
            }
        
        }
        col = append(col,row_min)
    }

    var ans  [] int
    
    for i:= 0 ; i< len(matrix);i ++ {
        for j:= 0; j< len(matrix[0]);j++{
            if row[i] == col[j]  && matrix[i][j] == col[j]  {
                ans = append(ans,col[j])
                
            } 
            
        
        }
    }
    

    


    // fmt.Println(ans)

    return ans


   


    
}