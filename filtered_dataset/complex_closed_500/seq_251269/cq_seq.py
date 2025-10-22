import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.07442, -0.01834).lineTo(0.0791, -0.01834).lineTo(0.0791, 0.01834).lineTo(0.07442, 0.01834).lineTo(0.07442, -0.01834).close()
solid=wp_sketch0.add(loop0).extrude(0.07778909178278051)
