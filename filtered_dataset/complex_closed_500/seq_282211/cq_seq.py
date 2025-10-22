import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00263, 0.00044).lineTo(-0.00262, 0.00044).lineTo(-0.00262, -0.00042).lineTo(0.00263, -0.00042).lineTo(0.00263, 0.00044).close()
solid=wp_sketch0.add(loop0).extrude(0.014224223738934616)
