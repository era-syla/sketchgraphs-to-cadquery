import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0006, 0.007).lineTo(0.0016, 0.007).lineTo(0.0016, 0.004).lineTo(0.0006, 0.004).lineTo(0.0006, 0.007).close()
solid=wp_sketch0.add(loop0).extrude(-0.0028259603770838565)
