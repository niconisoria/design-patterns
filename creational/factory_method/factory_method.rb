class Product
    def operation
        raise NotImplementedError, "#{self.class} has not implemented method '#{__method__}'"
    end
end

class ConcreteProductA < Product
    def operation
        '{Result of the ConcreteProductA}'
    end
end

class ConcreteProductB < Product
    def operation
        '{Result of the ConcreteProductB}'
    end
end

class Creator
    def factory_method
        raise NotImplementedError, "#{self.class} has not implemented method '#{__method__}'"
    end

    def some_operation
        product = factory_method
        result = product.operation
    end
end

class ConcreteCreatorA < Creator
    def factory_method
        ConcreteProductA.new
    end
end

class ConcreteCreatorB < Creator
    def factory_method
        ConcreteProductB.new
    end
end

def client_code(creator)
    print "Client: I'm not aware of the creator's class, but it still works.\n"\
          "#{creator.some_operation}"
end

client_code(ConcreteCreatorA.new)

