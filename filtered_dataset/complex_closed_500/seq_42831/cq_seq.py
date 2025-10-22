import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.07304, 0.03944).lineTo(0.01586, 0.03944).lineTo(0.01586, 0.00134).lineTo(-0.07304, 0.00134).lineTo(-0.07304, 0.03944).close()
solid=wp_sketch0.add(loop0).extrude(-0.1052804750798726)
