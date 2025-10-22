import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0025, 0.02).lineTo(0.0065, 0.02).lineTo(0.0065, 0.001).lineTo(0.0025, 0.001).lineTo(0.0025, 0.02).close()
solid=wp_sketch0.add(loop0).extrude(-0.03312050545172446)
