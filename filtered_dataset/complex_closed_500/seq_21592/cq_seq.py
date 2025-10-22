import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.008, 0.0).lineTo(0.008, 0.017).lineTo(0.005, 0.017).lineTo(0.005, 0.004).lineTo(0.0, 0.004).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.040201636604386345)
