import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.06197, -0.0254).lineTo(0.07063, -0.0254).lineTo(0.07063, -0.00414).lineTo(0.06197, -0.00414).lineTo(0.06197, -0.0254).close()
solid=wp_sketch0.add(loop0).extrude(0.009129120078548608)
