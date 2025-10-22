import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.12, -0.256).lineTo(0.298, -0.256).lineTo(0.298, -0.126).lineTo(0.12, -0.126).lineTo(0.12, -0.256).close()
solid=wp_sketch0.add(loop0).extrude(0.5241079371135363)
