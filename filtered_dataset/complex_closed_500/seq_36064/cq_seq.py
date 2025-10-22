import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.02687, 0.061).lineTo(0.02987, 0.061).lineTo(0.02987, 0.06325).lineTo(0.02687, 0.06325).lineTo(0.02687, 0.061).close()
solid=wp_sketch0.add(loop0).extrude(0.0006430612022949063)
