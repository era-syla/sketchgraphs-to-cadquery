import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.007, -0.019).lineTo(-0.007, -0.019).lineTo(-0.007, -0.016).lineTo(0.007, -0.016).lineTo(0.007, -0.019).close()
solid=wp_sketch0.add(loop0).extrude(0.021095719412007663)
