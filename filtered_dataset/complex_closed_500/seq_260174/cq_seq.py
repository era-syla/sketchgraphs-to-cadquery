import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.07099, 0.21).lineTo(0.07349, 0.21).lineTo(0.07349, 0.2035).lineTo(0.07099, 0.2035).lineTo(0.07099, 0.21).close()
solid=wp_sketch0.add(loop0).extrude(0.007654303248035071)
