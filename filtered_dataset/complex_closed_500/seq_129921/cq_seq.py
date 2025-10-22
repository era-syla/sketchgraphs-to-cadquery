import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(12.00912, 4.29768).lineTo(10.33272, 4.29768).lineTo(10.33272, 1.40208).lineTo(12.00912, 1.40208).lineTo(12.00912, 2.01168).lineTo(10.94232, 2.01168).lineTo(10.94232, 3.84048).lineTo(12.00912, 3.84048).lineTo(12.00912, 4.29768).close()
solid=wp_sketch0.add(loop0).extrude(-5.050905994717563)
