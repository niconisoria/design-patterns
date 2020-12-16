class Singleton
  private_class_method :new
  @instance = new

  def self.instance
    @instance
  end

  def business_logic
    # ...
  end
end

s1 = Singleton.instance
s2 = Singleton.instance

if s1.equal?(s2)
  print 'Singleton works, both variables contain the same instance.'
else
  print 'Singleton failed, variables contain different instances.'
end
