import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.30479, 0.0).lineTo(0.30479, 0.07638).lineTo(0.18783, 0.07638).lineTo(0.18783, 0.06738).lineTo(0.18086, 0.06738).lineTo(0.18086, 0.07638).lineTo(0.0, 0.07638).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.037574600546752296)
