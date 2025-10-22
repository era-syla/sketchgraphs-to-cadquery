import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0508, 0.0).lineTo(0.15875, 0.0635).lineTo(0.0508, 0.0635).lineTo(0.0508, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.311237771278566)
