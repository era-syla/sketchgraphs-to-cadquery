import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.06825, -0.0013).lineTo(0.04192, -0.0165).lineTo(0.0, -0.0165).lineTo(-0.04192, -0.0165).lineTo(-0.06825, -0.0013).lineTo(-0.06675, 0.0013).lineTo(-0.04112, -0.0135).lineTo(0.0, -0.0135).lineTo(0.04112, -0.0135).lineTo(0.06675, 0.0013).lineTo(0.06825, -0.0013).close()
solid=wp_sketch0.add(loop0).extrude(0.02819594897108525)
