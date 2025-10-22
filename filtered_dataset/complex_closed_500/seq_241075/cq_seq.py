import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0165, 0.015).lineTo(-0.0115, 0.018).lineTo(-0.0115, 0.04).lineTo(-0.0165, 0.04).lineTo(-0.0165, 0.015).close()
solid=wp_sketch0.add(loop0).extrude(-0.05780274108747727)
