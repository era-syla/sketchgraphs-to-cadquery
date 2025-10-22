import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.048).lineTo(0.012, 0.048).lineTo(0.012, 0.857).lineTo(0.0, 0.857).lineTo(0.0, 0.048).close()
solid=wp_sketch0.add(loop0).extrude(0.72379764158672)
