import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.04023, 0.00883).lineTo(-0.03251, 0.00883).lineTo(-0.03251, -0.0082).lineTo(-0.04023, -0.0082).lineTo(-0.04023, 0.00883).close()
solid=wp_sketch0.add(loop0).extrude(-0.0016931391857181873)
