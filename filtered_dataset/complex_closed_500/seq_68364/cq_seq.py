import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00075, 0.0025).lineTo(0.00075, 0.0025).lineTo(0.00075, 0.004).lineTo(-0.00075, 0.004).lineTo(-0.00075, 0.0025).close()
solid=wp_sketch0.add(loop0).extrude(-0.0003539623479131313)
