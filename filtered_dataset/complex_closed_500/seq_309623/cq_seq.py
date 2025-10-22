import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(4.0005, 0.0).lineTo(3.9624, 0.0).lineTo(3.9624, 0.0635).lineTo(4.0005, 0.0635).lineTo(4.0005, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.03784955927876273)
