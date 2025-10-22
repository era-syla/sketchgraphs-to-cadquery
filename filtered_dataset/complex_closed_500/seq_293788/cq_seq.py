import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.01265, 0.05442).lineTo(0.01455, 0.05442).lineTo(0.01455, 0.04172).lineTo(0.01265, 0.04172).lineTo(0.01265, 0.05442).close()
solid=wp_sketch0.add(loop0).extrude(0.012105961053378623)
