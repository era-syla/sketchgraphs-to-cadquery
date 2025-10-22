import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.03115, 0.0).lineTo(-0.03115, -0.0088).lineTo(-0.0285, 0.0).lineTo(-0.03115, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.008138387028639296)
