import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.007, -0.0345).lineTo(0.01096, -0.0345).lineTo(0.01096, -0.03679).lineTo(0.007, -0.0345).close()
solid=wp_sketch0.add(loop0).extrude(0.00711426076246508)
