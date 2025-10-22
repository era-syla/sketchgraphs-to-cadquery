import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.04).lineTo(0.04, 0.04).lineTo(0.08, 0.0).lineTo(0.08, -0.04).lineTo(0.04, -0.04).lineTo(-0.04, -0.04).lineTo(-0.04, 0.0).lineTo(0.0, 0.04).close()
solid=wp_sketch0.add(loop0).extrude(0.11257519710742844)
