import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.04008, 0.00317).lineTo(-0.00749, 0.00317).lineTo(-0.00749, -0.0127).lineTo(-0.04008, -0.0127).lineTo(-0.04008, 0.00317).close()
solid=wp_sketch0.add(loop0).extrude(-0.06247411254865852)
