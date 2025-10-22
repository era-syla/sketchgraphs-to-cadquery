import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0085, -0.011).lineTo(-0.00925, -0.011).lineTo(-0.00925, -0.02292).lineTo(-0.00483, -0.02292).lineTo(0.0085, -0.011).close()
solid=wp_sketch0.add(loop0).extrude(0.04228287578557804)
