import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.11684).lineTo(0.20574, 0.11684).lineTo(0.20574, -0.11684).lineTo(0.0, -0.11684).lineTo(0.0, 0.11684).close()
solid=wp_sketch0.add(loop0).extrude(0.6906324359702583)
