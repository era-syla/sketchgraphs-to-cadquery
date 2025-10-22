import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(7.92, 5.07).lineTo(7.86, 5.07).lineTo(7.86, 4.39).lineTo(7.92, 4.39).lineTo(7.92, 5.07).close()
solid=wp_sketch0.add(loop0).extrude(-1.0603719935320637)
