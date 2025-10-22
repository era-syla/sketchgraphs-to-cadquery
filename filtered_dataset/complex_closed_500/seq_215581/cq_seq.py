import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0047, -0.01).lineTo(-0.0115, -0.01).lineTo(-0.0115, -0.0041).lineTo(-0.0047, -0.0041).lineTo(-0.0047, -0.01).close()
solid=wp_sketch0.add(loop0).extrude(0.01275019065627696)
