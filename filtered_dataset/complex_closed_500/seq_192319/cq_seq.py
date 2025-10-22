import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.05928, 0.08916).lineTo(0.06772, 0.08916).lineTo(0.06772, -0.05689).lineTo(-0.05928, -0.05689).lineTo(-0.05928, 0.08916).close()
solid=wp_sketch0.add(loop0).extrude(0.08337304332180767)
