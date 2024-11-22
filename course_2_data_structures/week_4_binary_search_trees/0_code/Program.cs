using System;

class Program
{
    static void Main(string[] args)
    {
        BST<int> bst = new BST<int>();

        bst.Insert(new Key<int>(5), new Value("Five"));
        bst.Insert(new Key<int>(3), new Value("Three"));
        bst.Insert(new Key<int>(7), new Value("Seven"));
        bst.Insert(new Key<int>(2), new Value("Two"));
        bst.Insert(new Key<int>(4), new Value("Four"));
        bst.Insert(new Key<int>(6), new Value("Six"));
        bst.Insert(new Key<int>(8), new Value("Eight"));

        Console.WriteLine("In-order traversal:");
        bst.InOrderTraversal();

        Console.WriteLine("Search for key 4:");
        Value? val = bst.Search(new Key<int>(4));
        if (val != null)
        {
            Console.WriteLine(val.Data);
        }
        else
        {
            Console.WriteLine("Key not found");
        }

        Console.WriteLine("Print tree:");
        bst.Print();
        /*
        Print tree:
        │       ┌── Eight
        │   ┌── Seven
        │   │   └── Six
        └── Five
            │   ┌── Four
            └── Three
        */
    }
}

public class Key<T>
    where T : IComparable<T>
{
    public T Value { get; set; }

    public Key(T value)
    {
        Value = value;
    }

    public int CompareTo(Key<T> other)
    {
        return Value.CompareTo(other.Value);
    }
}

public class Value
{
    public string Data { get; set; }

    public Value(string data)
    {
        Data = data;
    }
}

public class Node<T>
    where T : IComparable<T>
{
    public Key<T> Key { get; set; }
    public Value Val { get; set; }
    public Node<T>? Left { get; set; }
    public Node<T>? Right { get; set; }

    public Node(Key<T> key, Value val)
    {
        Key = key;
        Val = val;
        Left = null;
        Right = null;
    }
}

public class BST<T>
    where T : IComparable<T>
{
    private Node<T>? root;

    public BST()
    {
        root = null;
    }

    // TODO: implement the following methods
    // get max value
    // get height
    // get node count
    // get successor

    public void Insert(Key<T> key, Value val)
    {
        root = Insert(root, key, val);
    }

    private Node<T> Insert(Node<T>? node, Key<T> key, Value val)
    {
        if (node == null)
        {
            return new Node<T>(key, val);
        }

        if (key.CompareTo(node.Key) < 0)
        {
            node.Left = Insert(node.Left, key, val);
        }
        else if (key.CompareTo(node.Key) > 0)
        {
            node.Right = Insert(node.Right, key, val);
        }
        else
        {
            node.Val = val;
        }

        return node;
    }

    public Value? Search(Key<T> key)
    {
        return Search(root, key);
    }

    private Value? Search(Node<T>? node, Key<T> key)
    {
        if (node == null)
        {
            return null;
        }

        if (key.CompareTo(node.Key) < 0)
        {
            return Search(node.Left, key);
        }
        else if (key.CompareTo(node.Key) > 0)
        {
            return Search(node.Right, key);
        }
        else
        {
            return node.Val;
        }
    }

    public void Delete(Key<T> key)
    {
        root = Delete(root, key);
    }

    private Node<T>? Delete(Node<T>? node, Key<T> key)
    {
        if (node == null)
        {
            return null;
        }

        if (key.CompareTo(node.Key) < 0)
        {
            node.Left = Delete(node.Left, key);
        }
        else if (key.CompareTo(node.Key) > 0)
        {
            node.Right = Delete(node.Right, key);
        }
        else
        {
            if (node.Left == null)
            {
                return node.Right;
            }
            else if (node.Right == null)
            {
                return node.Left;
            }
            else
            {
                Node<T> temp = MinValueNode(node.Right);
                node.Key = temp.Key;
                node.Val = temp.Val;
                node.Right = Delete(node.Right, temp.Key);
            }
        }

        return node;
    }

    private Node<T> MinValueNode(Node<T> node)
    {
        Node<T> current = node;

        while (current.Left != null)
        {
            current = current.Left;
        }

        return current;
    }

    public void InOrderTraversal()
    {
        InOrderTraversal(root);
    }

    private void InOrderTraversal(Node<T>? node)
    {
        if (node != null)
        {
            InOrderTraversal(node.Left);
            Console.WriteLine(node.Key.Value + " " + node.Val.Data);
            InOrderTraversal(node.Right);
        }
    }

    public void Print()
    {
        Print(root, "", true);
    }

    // WARN: so cool
    private void Print(Node<T>? node, string prefix = "", bool isLeft = true)
    {
        if (node == null)
        {
            return;
        }

        if (node.Right != null)
        {
            Print(node.Right, isLeft ? $"{prefix}│   " : $"{prefix}    ", false);
        }

        Console.WriteLine(isLeft ? $"{prefix}└── {node.Val.Data}" : $"{prefix}┌── {node.Val.Data}");

        if (node.Right != null)
        {
            Print(node.Left, isLeft ? $"{prefix}    " : $"{prefix}│   ", true);
        }
    }
}
