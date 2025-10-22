import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00838, 0.09447).lineTo(0.00927, 0.09447).lineTo(0.00927, 0.07571).lineTo(-0.00838, 0.07571).lineTo(-0.00838, 0.09447).close()
solid=wp_sketch0.add(loop0).extrude(0.024043031210180022)
