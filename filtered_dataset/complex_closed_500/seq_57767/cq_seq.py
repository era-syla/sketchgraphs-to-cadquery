import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.02931, 0.01854).lineTo(0.12069, 0.01854).lineTo(0.12069, -0.03146).lineTo(-0.02931, -0.03146).lineTo(-0.02931, 0.01854).close()
solid=wp_sketch0.add(loop0).extrude(0.0039103848025272775)
