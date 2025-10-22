import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(-0.01214, 0.0).lineTo(-0.01776, -0.01206).lineTo(-0.01445, -0.01206).lineTo(-0.01023, -0.003).lineTo(-0.00471, -0.003).lineTo(-0.00999, -0.01433).lineTo(-0.00668, -0.01433).lineTo(-0.0, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.02703840117624753)
