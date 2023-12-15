package dojo;

import java.util.ArrayList;
import java.util.List;

public class Order {

    private String owner;
    private String target;
    private List<String> cocktails;
    private String message;

    public void declareOwner(String string){
        this.owner = string;
    }

    public void declareTarget(String string){
        this.target = string;
    }

    public List<String> getCocktails(int number){
        if (number ==0) {
            this.cocktails = new ArrayList<String>();
        }else{
            this.cocktails = new ArrayList<String>(number);
        }

        return this.cocktails;
    }
}