import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0065, 0.0221).lineTo(-0.0065, 0.0221).lineTo(-0.0065, 0.01345).lineTo(0.0065, 0.01345).lineTo(0.0065, 0.0221).close()
solid=wp_sketch0.add(loop0).extrude(0.0013678650883220107)
