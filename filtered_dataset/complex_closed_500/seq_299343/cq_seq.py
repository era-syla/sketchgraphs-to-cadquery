import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(7.493, 1.8288).lineTo(7.493, -0.0).lineTo(7.62, -0.0).lineTo(7.62, 1.8288).lineTo(7.493, 1.8288).close()
solid=wp_sketch0.add(loop0).extrude(3.214893447425588)
