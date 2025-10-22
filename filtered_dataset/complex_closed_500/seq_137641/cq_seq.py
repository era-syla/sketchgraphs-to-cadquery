import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00482, 0.0304).lineTo(-0.00164, 0.0304).lineTo(-0.00164, 0.01455).lineTo(-0.00482, 0.01455).lineTo(-0.00482, 0.0304).close()
solid=wp_sketch0.add(loop0).extrude(-0.007003175165822705)
