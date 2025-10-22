import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-7.4168, 5.7658).lineTo(-8.9916, 5.7658).lineTo(-8.9916, 5.969).lineTo(-10.1092, 5.969).lineTo(-10.1092, 5.7658).lineTo(-11.684, 5.7658).lineTo(-9.5504, 7.8994).lineTo(-7.4168, 5.7658).close()
solid=wp_sketch0.add(loop0).extrude(3.51812658914369)
