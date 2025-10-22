import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.074, 0.0).lineTo(0.074, -0.00349).lineTo(0.03, -0.0).lineTo(0.074, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.04061565390132637)
