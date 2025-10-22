import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00672, -0.00672).lineTo(0.00672, -0.00672).lineTo(0.00672, 0.00672).lineTo(-0.00672, 0.00672).lineTo(-0.00672, -0.00672).close()
solid=wp_sketch0.add(loop0).extrude(0.01905875089365797)
