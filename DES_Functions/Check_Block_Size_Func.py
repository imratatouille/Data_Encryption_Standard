def check_block_size_func(bin_result_PT_len, bin_result_PT):
    block = []
    blocks = []
    if bin_result_PT_len == 64:
        block.extend(bin_result_PT)
        blocks.append(block)
        print("\nwrite bits == 64 bits", block)
        block_size = len(blocks)
        return blocks, block_size
        
    elif bin_result_PT_len > 64:
        block.extend(bin_result_PT)
        for i in range(0, len(block), 64):
            bin_chunk = block[i:i+64]
            if len(bin_chunk) != 64:
                bin_chunk.extend([0] * (64 - len(bin_chunk)))
            blocks.append(bin_chunk)
        print("\ninput bits > 64 bits")
        block_size = len(blocks)
        return blocks, block_size
        
    else:
        block.extend(bin_result_PT)
        while len(block) < 64:
            block.append(0)
        blocks.append(block)
        print("\ninput bits < 64 bits")
        block_size = len(blocks)
        return blocks, block_size