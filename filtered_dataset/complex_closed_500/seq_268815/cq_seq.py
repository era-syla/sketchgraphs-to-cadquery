import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.045, 0.0).lineTo(0.045, 0.145).lineTo(-0.0, 0.145).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.007922564153628632)
