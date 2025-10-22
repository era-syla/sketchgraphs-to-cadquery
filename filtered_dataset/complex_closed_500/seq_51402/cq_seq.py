import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.07779, 0.00953).lineTo(-0.07779, 0.00953).lineTo(-0.07779, -0.00953).lineTo(0.07779, -0.00953).lineTo(0.07779, 0.00953).close()
solid=wp_sketch0.add(loop0).extrude(0.10081405247434252)
