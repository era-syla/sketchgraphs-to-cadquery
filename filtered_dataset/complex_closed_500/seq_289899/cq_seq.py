import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(1.394, 2.40271).lineTo(-2.36659, 2.23695).lineTo(-2.3613, 2.11707).lineTo(1.39928, 2.28283).lineTo(1.394, 2.40271).close()
solid=wp_sketch0.add(loop0).extrude(-1.655308683470965)
