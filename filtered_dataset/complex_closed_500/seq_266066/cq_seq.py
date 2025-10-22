import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.12215, 0.06579).lineTo(0.13185, 0.06579).lineTo(0.13185, -0.03581).lineTo(-0.12215, -0.03581).lineTo(-0.12215, 0.06579).close()
solid=wp_sketch0.add(loop0).extrude(0.70602759817712)
